import React, {useEffect} from 'react';
import {View, Text, StyleSheet, Image} from 'react-native';
import {ActivityIndicator} from 'react-native-paper';

const SplashScreen = ({navigation}) => {
  useEffect(() => {
    setTimeout(() => {
      navigation.replace('Login');
    }, 2500);
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.appName}>उल्फत</Text>
      <Text style={styles.subtitle}>Ulfat - Shayari</Text>
      <Text style={styles.tagline}>शेर-ओ-शायरी का खज़ाना</Text>
      <ActivityIndicator size="large" color="#8B4789" style={styles.loader} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
  },
  appName: {
    fontSize: 56,
    fontWeight: 'bold',
    color: '#8B4789',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 20,
    color: '#666',
    marginBottom: 5,
  },
  tagline: {
    fontSize: 16,
    color: '#999',
    fontStyle: 'italic',
  },
  loader: {
    marginTop: 30,
  },
});

export default SplashScreen;
