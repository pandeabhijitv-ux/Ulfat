import React, {useState} from 'react';
import {View, Text, StyleSheet, TouchableOpacity, ScrollView} from 'react-native';
import {Button, Checkbox} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {categories} from '../data/shayariData';

const CategoryScreen = ({navigation}) => {
  const [selectedCategories, setSelectedCategories] = useState([]);

  const toggleCategory = catId => {
    if (selectedCategories.includes(catId)) {
      setSelectedCategories(selectedCategories.filter(id => id !== catId));
    } else {
      setSelectedCategories([...selectedCategories, catId]);
    }
  };

  const handleContinue = async () => {
    if (selectedCategories.length > 0) {
      await AsyncStorage.setItem(
        'selectedCategories',
        JSON.stringify(selectedCategories),
      );
      navigation.replace('Home');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>श्रेणी चुनें</Text>
      <Text style={styles.subtitle}>Select Your Favorite Categories</Text>

      <ScrollView style={styles.categoryList}>
        {categories.map(cat => (
          <TouchableOpacity
            key={cat.id}
            style={[
              styles.categoryCard,
              selectedCategories.includes(cat.id) && styles.selectedCard,
            ]}
            onPress={() => toggleCategory(cat.id)}>
            <View style={styles.categoryContent}>
              <Text style={styles.icon}>{cat.icon}</Text>
              <Text style={styles.categoryLabel}>{cat.label}</Text>
            </View>
            <Checkbox
              status={
                selectedCategories.includes(cat.id) ? 'checked' : 'unchecked'
              }
              onPress={() => toggleCategory(cat.id)}
            />
          </TouchableOpacity>
        ))}
      </ScrollView>

      <Button
        mode="contained"
        onPress={handleContinue}
        style={styles.button}
        disabled={selectedCategories.length === 0}>
        शुरू करें (Start Reading)
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#F5F5F5',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#8B4789',
    textAlign: 'center',
    marginTop: 40,
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 30,
  },
  categoryList: {
    flex: 1,
  },
  categoryCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#FFFFFF',
    padding: 20,
    marginBottom: 15,
    borderRadius: 12,
    elevation: 2,
    borderWidth: 2,
    borderColor: 'transparent',
  },
  selectedCard: {
    borderColor: '#8B4789',
    backgroundColor: '#F3E5F5',
  },
  categoryContent: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  icon: {
    fontSize: 32,
    marginRight: 15,
  },
  categoryLabel: {
    fontSize: 20,
    color: '#333',
    fontWeight: '500',
  },
  button: {
    marginTop: 20,
    paddingVertical: 8,
  },
});

export default CategoryScreen;
