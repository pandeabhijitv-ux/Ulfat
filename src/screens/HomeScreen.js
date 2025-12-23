import React, {useState, useEffect} from 'react';
import {View, Text, StyleSheet, FlatList, TouchableOpacity, RefreshControl} from 'react-native';
import {Appbar, Card, FAB, Searchbar, Banner, ActivityIndicator} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';
import FirebaseService from '../services/FirebaseService';

const HomeScreen = ({navigation}) => {
  const [allShayari, setAllShayari] = useState([]);
  const [filteredShayari, setFilteredShayari] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [userName, setUserName] = useState('');
  const [refreshing, setRefreshing] = useState(false);
  const [showSyncBanner, setShowSyncBanner] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
    checkForUpdates();
  }, []);

  const loadData = async () => {
    const name = await AsyncStorage.getItem('userName');
    setUserName(name || 'Guest');

    // Get shayari from cache or sync
    const shayari = await FirebaseService.getCachedShayari();
    setAllShayari(shayari);

    // Filter based on preferences
    const selectedLangs = JSON.parse(
      await AsyncStorage.getItem('selectedLanguages'),
    );
    const selectedCats = JSON.parse(
      await AsyncStorage.getItem('selectedCategories'),
    );

    const filtered = shayari.filter(
      item =>
        selectedLangs.includes(item.language) &&
        selectedCats.includes(item.category),
    );
    setFilteredShayari(filtered);
    setLoading(false);
  };

  const checkForUpdates = async () => {
    const needsSync = await FirebaseService.shouldSync();
    if (needsSync) {
      setShowSyncBanner(true);
    }
  };

  const handleSync = async () => {
    setShowSyncBanner(false);
    setRefreshing(true);
    await FirebaseService.syncShayari();
    await loadData();
    setRefreshing(false);
  };

  const onRefresh = async () => {
    await handleSync();
  };

  const onSearch = query => {
    setSearchQuery(query);
    if (query.trim() === '') {
      loadData();
    } else {
      const results = allShayari.filter(
        item =>
          item.text.toLowerCase().includes(query.toLowerCase()) ||
          item.author.toLowerCase().includes(query.toLowerCase()),
      );
      setFilteredShayari(results);
    }
  };

  const renderShayariCard = ({item}) => (
    <TouchableOpacity
      onPress={() => navigation.navigate('ShayariView', {shayariId: item.id, allShayari})}>
      <Card style={styles.card}>
        <Card.Content>
          <Text style={styles.shayariText} numberOfLines={3}>
            {item.text}
          </Text>
          <Text style={styles.author}>- {item.author}</Text>
        </Card.Content>
      </Card>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={[styles.container, styles.centered]}>
        <ActivityIndicator size="large" color="#8B4789" />
        <Text style={styles.loadingText}>शायरी लोड हो रही है...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Appbar.Header>
        <Appbar.Content title={`नमस्ते, ${userName}`} />
        <Appbar.Action
          icon="heart"
          onPress={() => navigation.navigate('Favorites')}
        />
        <Appbar.Action
          icon="cog"
          onPress={() => navigation.navigate('AdminPanel')}
        />
      </Appbar.Header>

      <Banner
        visible={showSyncBanner}
        actions={[
          {
            label: 'अभी अपडेट करें',
            onPress: handleSync,
          },
          {
            label: 'बाद में',
            onPress: () => setShowSyncBanner(false),
          },
        ]}
        icon="cloud-download">
        नयी शायरी उपलब्ध है! अपडेट करें
      </Banner>

      <Searchbar
        placeholder="शायरी खोजें (Search Shayari)"
        onChangeText={onSearch}
        value={searchQuery}
        style={styles.searchbar}
      />

      <Text style={styles.counter}>
        📚 कुल शायरी: {allShayari.length} | दिखाई दे रही: {filteredShayari.length}
      </Text>

      <FlatList
        data={filteredShayari}
        renderItem={renderShayariCard}
        keyExtractor={item => item.id.toString()}
        contentContainerStyle={styles.list}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
      />

      <FAB
        style={styles.fab}
        icon="shuffle-variant"
        label="Random"
        onPress={() => {
          const randomItem =
            filteredShayari[Math.floor(Math.random() * filteredShayari.length)];
          navigation.navigate('ShayariView', {shayariId: randomItem.id, allShayari});
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  centered: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 15,
    fontSize: 16,
    color: '#666',
  },
  searchbar: {
    margin: 15,
    marginBottom: 10,
    elevation: 2,
  },
  counter: {
    textAlign: 'center',
    color: '#666',
    fontSize: 13,
    marginBottom: 10,
  },
  list: {
    padding: 15,
    paddingBottom: 80,
  },
  card: {
    marginBottom: 15,
    elevation: 3,
  },
  shayariText: {
    fontSize: 18,
    lineHeight: 28,
    color: '#333',
    fontWeight: '500',
  },
  author: {
    fontSize: 14,
    color: '#8B4789',
    marginTop: 10,
    fontStyle: 'italic',
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
    backgroundColor: '#8B4789',
  },
});

export default HomeScreen;
