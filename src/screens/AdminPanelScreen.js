import React, {useState} from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  Alert,
  KeyboardAvoidingView,
} from 'react-native';
import {
  Appbar,
  TextInput,
  Button,
  RadioButton,
  HelperText,
  Snackbar,
} from 'react-native-paper';
import FirebaseService from '../services/FirebaseService';
import {categories, languages} from '../data/shayariData';

const AdminPanelScreen = ({navigation}) => {
  const [shayariText, setShayariText] = useState('');
  const [author, setAuthor] = useState('');
  const [language, setLanguage] = useState('hindi');
  const [category, setCategory] = useState('romantic');
  const [uploading, setUploading] = useState(false);
  const [snackbarVisible, setSnackbarVisible] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');

  const handleSubmit = async () => {
    if (!shayariText.trim() || !author.trim()) {
      Alert.alert('Error', 'कृपया सभी फील्ड्स भरें');
      return;
    }

    setUploading(true);

    const newShayari = {
      id: Date.now(),
      text: shayariText.trim(),
      author: author.trim(),
      language,
      category,
      createdAt: new Date().toISOString(),
    };

    const success = await FirebaseService.uploadShayari(newShayari);

    setUploading(false);

    if (success) {
      setSnackbarMessage('✅ शायरी सफलतापूर्वक जोड़ी गई!');
      setSnackbarVisible(true);
      // Clear form
      setShayariText('');
      setAuthor('');
      setLanguage('hindi');
      setCategory('romantic');
    } else {
      Alert.alert('Error', 'शायरी अपलोड करने में त्रुटि');
    }
  };

  return (
    <View style={styles.container}>
      <Appbar.Header>
        <Appbar.BackAction onPress={() => navigation.goBack()} />
        <Appbar.Content title="Admin Panel - Add Shayari" />
      </Appbar.Header>

      <KeyboardAvoidingView behavior="padding" style={{flex: 1}}>
        <ScrollView contentContainerStyle={styles.content}>
          <Text style={styles.sectionTitle}>नयी शायरी जोड़ें</Text>

          <TextInput
            label="शायरी (Shayari Text)"
            value={shayariText}
            onChangeText={setShayariText}
            mode="outlined"
            multiline
            numberOfLines={6}
            style={styles.textArea}
            placeholder="शायरी यहाँ लिखें..."
          />

          <TextInput
            label="लेखक (Author)"
            value={author}
            onChangeText={setAuthor}
            mode="outlined"
            style={styles.input}
            placeholder="जैसे: Mirza Ghalib"
          />

          <Text style={styles.label}>भाषा (Language):</Text>
          <RadioButton.Group
            onValueChange={setLanguage}
            value={language}>
            {languages.map(lang => (
              <View key={lang.id} style={styles.radioItem}>
                <RadioButton value={lang.id} />
                <Text style={styles.radioLabel}>{lang.label}</Text>
              </View>
            ))}
          </RadioButton.Group>

          <Text style={styles.label}>श्रेणी (Category):</Text>
          <RadioButton.Group
            onValueChange={setCategory}
            value={category}>
            {categories.map(cat => (
              <View key={cat.id} style={styles.radioItem}>
                <RadioButton value={cat.id} />
                <Text style={styles.radioLabel}>
                  {cat.icon} {cat.label}
                </Text>
              </View>
            ))}
          </RadioButton.Group>

          <Button
            mode="contained"
            onPress={handleSubmit}
            loading={uploading}
            disabled={uploading}
            style={styles.submitButton}>
            {uploading ? 'अपलोड हो रहा है...' : 'शायरी जोड़ें (Submit)'}
          </Button>

          <HelperText type="info" style={styles.helper}>
            💡 यह शायरी 24 घंटे के भीतर सभी यूजर्स के ऐप में दिखाई देगी
          </HelperText>
        </ScrollView>
      </KeyboardAvoidingView>

      <Snackbar
        visible={snackbarVisible}
        onDismiss={() => setSnackbarVisible(false)}
        duration={3000}>
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
    padding: 20,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#8B4789',
    marginBottom: 20,
    textAlign: 'center',
  },
  textArea: {
    marginBottom: 15,
    minHeight: 150,
  },
  input: {
    marginBottom: 15,
  },
  label: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginTop: 10,
    marginBottom: 5,
  },
  radioItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 5,
  },
  radioLabel: {
    fontSize: 16,
    color: '#333',
  },
  submitButton: {
    marginTop: 20,
    paddingVertical: 8,
  },
  helper: {
    textAlign: 'center',
    marginTop: 10,
  },
});

export default AdminPanelScreen;
