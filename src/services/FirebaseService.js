// Firebase Service for Cloud Sync
import AsyncStorage from '@react-native-async-storage/async-storage';
import {shayariData as offlineData} from '../data/shayariData';

const FIREBASE_URL = 'https://ulfat-shayari-default-rtdb.firebaseio.com';
const LAST_SYNC_KEY = 'lastSyncDate';
const SHAYARI_CACHE_KEY = 'cachedShayari';

class FirebaseService {
  constructor() {
    this.baseUrl = FIREBASE_URL;
  }

  // Fetch new shayari from Firebase
  async fetchShayariFromCloud() {
    try {
      const response = await fetch(`${this.baseUrl}/shayari.json`);
      if (response.ok) {
        const data = await response.json();
        return data ? Object.values(data) : [];
      }
      return [];
    } catch (error) {
      console.error('Error fetching from cloud:', error);
      return [];
    }
  }

  // Check if we need to sync (once per day)
  async shouldSync() {
    const lastSync = await AsyncStorage.getItem(LAST_SYNC_KEY);
    if (!lastSync) return true;

    const lastSyncDate = new Date(lastSync);
    const now = new Date();
    const hoursDiff = (now - lastSyncDate) / (1000 * 60 * 60);

    // Sync if more than 24 hours
    return hoursDiff >= 24;
  }

  // Main sync function - downloads new shayari
  async syncShayari() {
    try {
      if (!(await this.shouldSync())) {
        console.log('Sync not needed yet');
        return await this.getCachedShayari();
      }

      console.log('Syncing shayari from cloud...');
      const cloudShayari = await this.fetchShayariFromCloud();

      let allShayari = [...offlineData];

      if (cloudShayari.length > 0) {
        // Merge cloud shayari with offline data
        const existingIds = new Set(offlineData.map(s => s.id));
        const newShayari = cloudShayari.filter(s => !existingIds.has(s.id));
        allShayari = [...offlineData, ...newShayari];

        console.log(`Added ${newShayari.length} new shayari from cloud`);
      }

      // Cache the merged data
      await AsyncStorage.setItem(SHAYARI_CACHE_KEY, JSON.stringify(allShayari));
      await AsyncStorage.setItem(LAST_SYNC_KEY, new Date().toISOString());

      return allShayari;
    } catch (error) {
      console.error('Sync error:', error);
      // Return offline data if sync fails
      return offlineData;
    }
  }

  // Get cached shayari or offline data
  async getCachedShayari() {
    try {
      const cached = await AsyncStorage.getItem(SHAYARI_CACHE_KEY);
      if (cached) {
        return JSON.parse(cached);
      }
    } catch (error) {
      console.error('Error reading cache:', error);
    }
    return offlineData;
  }

  // Upload new shayari to cloud (Admin function)
  async uploadShayari(shayari) {
    try {
      const response = await fetch(`${this.baseUrl}/shayari.json`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(shayari),
      });
      return response.ok;
    } catch (error) {
      console.error('Upload error:', error);
      return false;
    }
  }

  // Get total shayari count
  async getShayariCount() {
    const allShayari = await this.getCachedShayari();
    return allShayari.length;
  }

  // Force sync (manual refresh)
  async forceSync() {
    await AsyncStorage.removeItem(LAST_SYNC_KEY);
    return await this.syncShayari();
  }
}

export default new FirebaseService();
