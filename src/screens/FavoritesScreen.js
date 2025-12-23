import React, {useState, useEffect} from 'react';
import {View, Text, StyleSheet, FlatList, TouchableOpacity} from 'react-native';
import {Appbar, Card} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';
import FirebaseService from '../services/FirebaseService';

const FavoritesScreen = ({navigation}) => {
  const [favorites, setFavorites] = useState([]);
  const [allShayari, setAllShayari] = useState([]);

  useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      loadFavorites();
    });
    return unsubscribe;
  }, [navigation]);

  const loadFavorites = async () => {
    const shayariList = await FirebaseService.getCachedShayari();
    setAllShayari(shayariList);

    const favData = await AsyncStorage.getItem('favorites');
    if (favData) {
      const favIds = JSON.parse(favData);
      const favShayari = shayariList.filter(item => favIds.includes(item.id));
      setFavorites(favShayari);
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

  return (
    <View style={styles.container}>
      <Appbar.Header>
        <Appbar.BackAction onPress={() => navigation.goBack()} />
        <Appbar.Content title="पसंदीदा शायरी" />
      </Appbar.Header>

      {favorites.length === 0 ? (
        <View style={styles.emptyContainer}>
          <Text style={styles.emptyText}>
            कोई पसंदीदा शायरी नहीं है {'\n'}
            No favorites yet
          </Text>
        </View>
      ) : (
        <FlatList
          data={favorites}
          renderItem={renderShayariCard}
          keyExtractor={item => item.id.toString()}
          contentContainerStyle={styles.list}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  list: {
    padding: 15,
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
  emptyContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  emptyText: {
    fontSize: 18,
    color: '#999',
    textAlign: 'center',
  },
});

export default FavoritesScreen;
