import React from 'react';
import LoginScreen from './components/loginScreen.js'
import HomeScreen from './components/homeScreen.js'
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName = "LoginPage">
         <Stack.Screen name="LoginPage" options={{headerShown:false}} component={LoginScreen} />
         <Stack.Screen name="Home" options={{headerShown:false}} component={HomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
