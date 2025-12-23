import {MD3LightTheme} from 'react-native-paper';

export const theme = {
  ...MD3LightTheme,
  colors: {
    ...MD3LightTheme.colors,
    primary: '#8B4789',
    secondary: '#D4A5D4',
    background: '#F5F5F5',
    surface: '#FFFFFF',
    accent: '#9C27B0',
    text: '#212121',
    error: '#B00020',
  },
};

export const darkTheme = {
  ...theme,
  dark: true,
  colors: {
    ...theme.colors,
    primary: '#BB86FC',
    background: '#121212',
    surface: '#1E1E1E',
    text: '#FFFFFF',
  },
};
