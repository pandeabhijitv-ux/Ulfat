import React, {useState, useEffect} from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Share,
} from 'react-native';
import {Appbar, IconButton, Snackbar} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';
import FirebaseService from '../services/FirebaseService';

const ShayariViewScreen = ({route, navigation}) => {
  const {shayariId, allShayari: initialShayari} = route.params;
  const [shayariList, setShayariList] = useState(initialShayari || []);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFavorite, setIsFavorite] = useState(false);
  const [snackbarVisible, setSnackbarVisible] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');

  useEffect(() => {
    loadShayariList();
  }, []);

  const loadShayariList = async () => {
    const allShayari = await FirebaseService.getCachedShayari();
    setShayariList(allShayari);
    const index = allShayari.findIndex(item => item.id === shayariId);
    setCurrentIndex(index >= 0 ? index : 0);
    checkFavorite(shayariId);
  };

  const checkFavorite = async id => {
    const favorites = await AsyncStorage.getItem('favorites');
    if (favorites) {
      const favArray = JSON.parse(favorites);
      setIsFavorite(favArray.includes(id));
    }
  };

  const toggleFavorite = async () => {
    const currentShayari = shayariList[currentIndex];
    if (!currentShayari) return;

    let favorites = await AsyncStorage.getItem('favorites');
    let favArray = favorites ? JSON.parse(favorites) : [];

    if (isFavorite) {
      favArray = favArray.filter(id => id !== currentShayari.id);
      showSnackbar('पसंदीदा से हटाया गया');
    } else {
      favArray.push(currentShayari.id);
      showSnackbar('पसंदीदा में जोड़ा गया');
    }

    await AsyncStorage.setItem('favorites', JSON.stringify(favArray));
    setIsFavorite(!isFavorite);
  };

  const handleShare = async () => {
    const currentShayari = shayariList[currentIndex];
    if (!currentShayari) return;

    try {
      await Share.share({
        message: `${currentShayari.text}\n\n- ${currentShayari.author}\n\nशेयर किया गया उल्फत ऐप से 💕\n\nDownload Ulfat - Hindi, Urdu & Marathi Shayari App`,
      });
    } catch (error) {
      console.log(error);
    }
  };

  const showSnackbar = message => {
    setSnackbarMessage(message);
    setSnackbarVisible(true);
  };

  const goNext = () => {
    if (currentIndex < shayariList.length - 1) {
      setCurrentIndex(currentIndex + 1);
      checkFavorite(shayariList[currentIndex + 1].id);
    }
  };

  const goPrevious = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
      checkFavorite(shayariList[currentIndex - 1].id);
    }
  };

  const currentShayari = shayariList[currentIndex];

  if (!currentShayari) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Appbar.Header>
        <Appbar.BackAction onPress={() => navigation.goBack()} />
        <Appbar.Content title="शायरी" />
        <Appbar.Action
          icon={isFavorite ? 'heart' : 'heart-outline'}
          onPress={toggleFavorite}
        />
        <Appbar.Action icon="share-variant" onPress={handleShare} />
      </Appbar.Header>

      <ScrollView contentContainerStyle={styles.content}>
        <View style={styles.shayariContainer}>
          <Text style={styles.shayariText}>{currentShayari.text}</Text>
          <Text style={styles.author}>- {currentShayari.author}</Text>
        </View>

        <View style={styles.navigation}>
          <IconButton
            icon="chevron-left"
            size={40}
            onPress={goPrevious}
            disabled={currentIndex === 0}
            iconColor="#8B4789"
          />
          <Text style={styles.counter}>
            {currentIndex + 1} / {shayariList.length}
          </Text>
          <IconButton
            icon="chevron-right"
            size={40}
            onPress={goNext}
            disabled={currentIndex === shayariList.length - 1}
            iconColor="#8B4789"
          />
        </View>
      </ScrollView>

      <Snackbar
        visible={snackbarVisible}
        onDismiss={() => setSnackbarVisible(false)}
        duration={2000}>
        {snackbarMessage}
      </Snackbar>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  content: {
    flexGrow: 1,
    justifyContent: 'center',
    padding: 20,
  },
  shayariContainer: {
    backgroundColor: '#FFFFFF',
    padding: 30,
    borderRadius: 15,
    elevation: 5,
    minHeight: 300,
    justifyContent: 'center',
  },
  shayariText: {
    fontSize: 22,
    lineHeight: 38,
    color: '#333',
    textAlign: 'center',
    fontWeight: '500',
  },
  author: {
    fontSize: 16,
    color: '#8B4789',
    marginTop: 20,
    textAlign: 'right',
    fontStyle: 'italic',
  },
  navigation: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 30,
  },
  counter: {
    fontSize: 18,
    color: '#666',
    marginHorizontal: 20,
  },
});

export default ShayariViewScreen;
