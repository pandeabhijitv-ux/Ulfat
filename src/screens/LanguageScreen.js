import React, {useState} from 'react';
import {View, Text, StyleSheet, TouchableOpacity, ScrollView} from 'react-native';
import {Button, Checkbox} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {languages} from '../data/shayariData';

const LanguageScreen = ({navigation}) => {
  const [selectedLanguages, setSelectedLanguages] = useState([]);

  const toggleLanguage = langId => {
    if (selectedLanguages.includes(langId)) {
      setSelectedLanguages(selectedLanguages.filter(id => id !== langId));
    } else {
      setSelectedLanguages([...selectedLanguages, langId]);
    }
  };

  const handleContinue = async () => {
    if (selectedLanguages.length > 0) {
      await AsyncStorage.setItem(
        'selectedLanguages',
        JSON.stringify(selectedLanguages),
      );
      navigation.replace('Category');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>भाषा चुनें</Text>
      <Text style={styles.subtitle}>Select Your Preferred Languages</Text>

      <ScrollView style={styles.languageList}>
        {languages.map(lang => (
          <TouchableOpacity
            key={lang.id}
            style={[
              styles.languageCard,
              selectedLanguages.includes(lang.id) && styles.selectedCard,
            ]}
            onPress={() => toggleLanguage(lang.id)}>
            <View style={styles.languageContent}>
              <Text style={styles.flag}>{lang.flag}</Text>
              <Text style={styles.languageLabel}>{lang.label}</Text>
            </View>
            <Checkbox
              status={
                selectedLanguages.includes(lang.id) ? 'checked' : 'unchecked'
              }
              onPress={() => toggleLanguage(lang.id)}
            />
          </TouchableOpacity>
        ))}
      </ScrollView>

      <Button
        mode="contained"
        onPress={handleContinue}
        style={styles.button}
        disabled={selectedLanguages.length === 0}>
        जारी रखें (Continue)
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
  languageList: {
    flex: 1,
  },
  languageCard: {
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
  languageContent: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  flag: {
    fontSize: 32,
    marginRight: 15,
  },
  languageLabel: {
    fontSize: 24,
    color: '#333',
    fontWeight: '500',
  },
  button: {
    marginTop: 20,
    paddingVertical: 8,
  },
});

export default LanguageScreen;
