import React, {useState, useEffect} from 'react';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import {Provider as PaperProvider} from 'react-native-paper';
import SplashScreen from './screens/SplashScreen';
import LoginScreen from './screens/LoginScreen';
import HomeScreen from './screens/HomeScreen';
import LanguageScreen from './screens/LanguageScreen';
import CategoryScreen from './screens/CategoryScreen';
import ShayariViewScreen from './screens/ShayariViewScreen';
import FavoritesScreen from './screens/FavoritesScreen';
import AdminPanelScreen from './screens/AdminPanelScreen';
import {theme} from './config/theme';
import FirebaseService from './services/FirebaseService';

const Stack = createStackNavigator();

const App = () => {
  useEffect(() => {
    // Auto-sync shayari on app start
    FirebaseService.syncShayari();
  }, []);

  return (
    <PaperProvider theme={theme}>
      <NavigationContainer>
        <Stack.Navigator 
          initialRouteName="Splash"
          screenOptions={{
            headerShown: false,
          }}>
          <Stack.Screen name="Splash" component={SplashScreen} />
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Language" component={LanguageScreen} />
          <Stack.Screen name="Category" component={CategoryScreen} />
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="ShayariView" component={ShayariViewScreen} />
          <Stack.Screen name="Favorites" component={FavoritesScreen} />
          <Stack.Screen name="AdminPanel" component={AdminPanelScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    </PaperProvider>
  );
};

export default App;
