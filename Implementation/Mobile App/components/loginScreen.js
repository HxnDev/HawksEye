import React, { Component } from 'react'
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image ,TouchableHighlight, TextInput, TouchableOpacity, Button, CheckBox,ImageBackground } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Dimensions } from 'react-native'
import Ionicons from '@expo/vector-icons/Ionicons';
import FontAwesome from '@expo/vector-icons/FontAwesome';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import colors from '../config/colors';

class LoginScreen extends Component {
   constructor () {
      super();
      this.state = {
         email: '',
         password: '',
         keepIn : 'black',
      };
    }

   handleKeepSignedIn () {
     
      if (this.state.keepIn == 'black') {
         this.setState({ keepIn : '#28D8A1' });
      } else {
         this.setState({ keepIn : 'black' });
      }
      
   }

   handleEmail = (text) => {
      this.setState({ email: text })
   }
   handlePassword = (text) => {
      this.setState({ password: text })
   }
   login = (email, pass, navigation ) => {
      // alert('email: ' + email +'\n'+ 'password: ' + pass)
      this.props.navigation.navigate('Home')
   }

   forgotpassword = () =>{

    alert('Too bad Hun!')

   }

   loginWithGoogle = () => {
      console.log('Login with Google Button Pressed');
   }

   render() {
      return (
        <SafeAreaView style={styles.container}>

            {/* <Image style={styles.image}
            source={require('../assets/LoginScreen.jpg')}/> */}

            <ImageBackground source={require('../assets/BGfinal2.jpg')} resizeMode="cover" style={styles.imgcontainer}>

            <Text style={styles.LogoBaseText}>
               HAWK'S 
               <Text style={styles.LogoInnerText}> EYE</Text>
            </Text>

            <View style={styles.inputfield}>
            <Ionicons name="md-person" style = {styles.inputfieldicons} color={'white'} />
            <TextInput style = {styles.input}
               inlineImageLeft= 'search_icon' 
               underlineColorAndroid = "transparent"
               placeholder = "Email"
               placeholderTextColor = "white"
               autoCapitalize = "none"
               onChangeText = {this.handleEmail}/>
            </View>

            <View style={styles.inputfield}>
            <Ionicons name="md-lock-closed" style = {styles.inputfieldicons} color={'white'} />
            <TextInput style = {styles.input}
               underlineColorAndroid = "transparent"
               placeholder = "Password"
               placeholderTextColor = "white"
               autoCapitalize = "none"
               onChangeText = {this.handlePassword}/>
            </View>
               
            <View style={styles.checkbox}>
            <TouchableOpacity
               style = {styles.box}>
               <Ionicons name="md-checkmark" style = {styles.checkboxIcon} color={this.state.keepIn} onPress={this.handleKeepSignedIn.bind(this)} />
            </TouchableOpacity>
            <Text style = {styles.checkboxText}> Keep me Signed in</Text>
            </View>

            <TouchableOpacity
               style = {styles.submitButton}
               onPress = {
                  () => this.login(this.state.email, this.state.password)
               }>
               <Text style = {styles.submitButtonText}> Login </Text>
            </TouchableOpacity>

            <TouchableOpacity
               style = {styles.forgotPassword}
               onPress = {
                  () => this.forgotpassword()
               }>
               <Text style = {styles.forgotPasswordText}> Forgot Password? </Text>
            </TouchableOpacity>

            <View style={styles.googleLogin}>
               <FontAwesome.Button style={styles.icon} name="google" 
               onPress = {
                  () => this.loginWithGoogle()
               }>
               Login with Google
               </FontAwesome.Button>
            </View>
            </ImageBackground>
        </SafeAreaView>
      )
   }
}
export default LoginScreen

const styles = StyleSheet.create({
   container: {
        flex: 1,
        marginTop: StatusBar.currentHeight,
        backgroundColor: 'black',
        alignItems: 'center',
        justifyContent: 'center',
    },

    imgcontainer:{
      alignItems: 'center',
      justifyContent: 'center',
      width: Dimensions.get('window').width, 
      height: Dimensions.get('window').height,
    },

   input: {
   
        width: 230,
        paddingLeft:15,
        height: 40,
        color : "white",

        borderColor: 'transparent',
        borderWidth: 1,
        borderRadius: 7,
        backgroundColor: 'transparent',
        //opacity: .9,

        //elevation: 10,

   },

   // view container to include icons in the field 
   inputfield:{

      marginTop: 15,
      backgroundColor: '#212121',
      opacity: 0.7,
      flexDirection: 'row',
      justifyContent: 'center',
      alignItems: 'center',

      width: 250,
      borderRadius: 7,
   },

   inputfieldicons:{

      paddingLeft: 15,
      color: 'white',
      fontSize: 13,
   },

   //Login Button
   submitButton: {

        backgroundColor: colors.secondary,

        height: 40,
        //width: 250,
        //borderRadius: 7,

        width: 175,
        borderRadius: 30,

        //For the Text
        alignItems: 'center',
        justifyContent: 'center',

        shadowColor: 'white',
        shadowOpacity: 0.36,
        shadowOffset: { width: 10, height: 20},
        shadowRadius: 20,
        elevation: 7,
   },
   submitButtonText:{
        
        color: 'white',
        fontWeight: 'bold',
        fontSize: 16,
   },

   forgotPassword:{

        marginTop:20,
        //marginBottom: 15,
   },
   forgotPasswordText:{
        
        color: colors.primary,
    },

   LogoBaseText:{

      //fontFamily: 'lucida grande',
      fontSize: 43,
      fontWeight: "bold",
      color: colors.primary,
   },

   LogoInnerText:{

      //fontFamily: 'lucida grande',
      fontSize: 43,
      fontWeight: "bold",
      color: colors.secondary,
   },

   image:{

        width: 250 , 
        height: Dimensions.get('window').height,
        borderRadius: 7,

   },

   //Add Keep Me Signed In checkBox
   checkbox: {
      flexDirection: 'row',
      justifyContent: 'flex-start',
      alignItems: 'center',
      width: 250,
   },
   checkboxText: {
      fontSize: 13,
      color: colors.primary,
   },
   box: {
      marginTop: 10,
      marginBottom: 10, 
      marginRight: 10,
      backgroundColor: 'transparent',

      height: 25,
      width: 25,

      borderRadius: 7,
      borderColor: colors.primary ,
      borderWidth: 1.5,
      marginTop : 15,
      justifyContent: 'center',
      alignItems: 'center',
   },
   checkboxIcon:{

      paddingTop: 0,
      fontSize : 20,

   },

    //Check Box Code ends here
    icon: {
      height: 40,
      width: 250,
      backgroundColor :"#DB4437",
      justifyContent: 'center',
      alignItems: 'center',
    },

    googleLogin: {

      height: 40,
      width: 250,
      borderRadius: 30,
      marginTop: 20,
      shadowColor: 'white',
      shadowOpacity: 0.36,
      shadowOffset: { width: 10, height: 20},
      shadowRadius: 20,
      elevation: 7,

    },

})