import React, {useState} from 'react';
import {View, Text, StyleSheet, TouchableOpacity} from 'react-native';
import {TextInput, Button} from 'react-native-paper';
import AsyncStorage from '@react-native-async-storage/async-storage';

const LoginScreen = ({navigation}) => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');

  const handleLogin = async () => {
    if (name.trim()) {
      await AsyncStorage.setItem('userName', name);
      await AsyncStorage.setItem('userEmail', email || 'guest@ulfat.com');
      navigation.replace('Language');
    }
  };

  const handleSkip = async () => {
    await AsyncStorage.setItem('userName', 'Guest');
    await AsyncStorage.setItem('userEmail', 'guest@ulfat.com');
    navigation.replace('Language');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>स्वागत है</Text>
      <Text style={styles.subtitle}>Welcome to Ulfat</Text>

      <View style={styles.form}>
        <TextInput
          label="आपका नाम (Your Name)"
          value={name}
          onChangeText={setName}
          mode="outlined"
          style={styles.input}
        />
        <TextInput
          label="ईमेल (Email - Optional)"
          value={email}
          onChangeText={setEmail}
          mode="outlined"
          keyboardType="email-address"
          style={styles.input}
        />

        <Button
          mode="contained"
          onPress={handleLogin}
          style={styles.button}
          disabled={!name.trim()}>
          शुरू करें (Start)
        </Button>

        <TouchableOpacity onPress={handleSkip}>
          <Text style={styles.skipText}>अभी नहीं, बाद में (Skip for now)</Text>
        </TouchableOpacity>
      </View>

      <Text style={styles.footer}>
        By continuing, you agree to our Terms & Privacy Policy
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#F5F5F5',
    justifyContent: 'center',
  },
  title: {
    fontSize: 36,
    fontWeight: 'bold',
    color: '#8B4789',
    textAlign: 'center',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 18,
    color: '#666',
    textAlign: 'center',
    marginBottom: 40,
  },
  form: {
    marginBottom: 20,
  },
  input: {
    marginBottom: 15,
  },
  button: {
    marginTop: 10,
    paddingVertical: 8,
  },
  skipText: {
    textAlign: 'center',
    color: '#8B4789',
    marginTop: 20,
    fontSize: 16,
    textDecorationLine: 'underline',
  },
  footer: {
    textAlign: 'center',
    color: '#999',
    fontSize: 12,
    marginTop: 20,
  },
});

export default LoginScreen;
