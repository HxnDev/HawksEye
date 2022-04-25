import React, { Component } from 'react'
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image ,TouchableHighlight, TextInput, TouchableOpacity, Button, CheckBox  } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Dimensions } from 'react-native'

import Ionicons from '@expo/vector-icons/Ionicons';

import colors from '../config/colors';

class HomeScreen extends Component {
   constructor () {
      super();
      this.state = {
         priority: 'High\n',
         Room: '9A\n',
         Time: '9:00 am\n',
         Issue: 'Patient Fainted\n',
         space: '\n'
      };
    }

    ack = () => {
      alert('Do you acknowledge?');
   }

   handleLogout () {
      this.props.navigation.goBack('LoginPage')
   }

   render() {
      return (
         
        <SafeAreaView style={styles.container}>
            <View
               style={styles.appbars}>
               <TouchableOpacity backgroundColor='white' alignSelf = 'flex-end'>
                  <Ionicons name="md-close" style = {styles.iconLogout} onPress={this.handleLogout.bind(this)}/>
               </TouchableOpacity>   
            </View>

           <TouchableOpacity
               style = {styles.alertMessages}
               onPress = {
                  () => this.ack()
               }>
               <Text>{this.state.space}</Text> 
               <Ionicons name="md-alert-circle" style = {styles.icon} />
               <Text>{this.state.space}</Text> 

               <Text style={styles.alertText}>
                  Priority  : 
                  <Text style={styles.alertInfo}>  {this.state.priority}</Text>
               </Text>
               <Text style={styles.alertText}>
                  Issue     : 
                  <Text style={styles.alertInfo}>  {this.state.Issue}</Text>
               </Text>
               <Text style={styles.alertText}>
                  Room    :  
                  <Text style={styles.alertInfo}>  {this.state.Room}</Text>
               </Text>
               <Text style={styles.alertText}>
                  Time     :  
                  <Text style={styles.alertInfo}>  {this.state.Time}</Text>
               </Text>
               <Text>{this.state.space}</Text> 

               {/* <Text style = {styles.alertText}>Priority  : {this.state.priority}Issue     : {this.state.Issue}Room    : {this.state.Room}Time     : {this.state.Time}</Text> */}
            </TouchableOpacity>
            <View
               style={styles.appbars}>
               <Text style = {styles.plainText}>© 2022 by ThinkVision</Text> 
            </View>
            <StatusBar style="light" backgroundColor="black" />
        </SafeAreaView>
      )
   }
}
export default HomeScreen

const styles = StyleSheet.create({
   container: {
        flex: 1,
        marginTop: StatusBar.currentHeight,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'space-between',
    },

    appbars:{

      height: 50 ,
      width: Dimensions.get('window').width,
      backgroundColor: 'black',
      justifyContent: 'center',
      
    },

   alertMessages: {
      backgroundColor: colors.ora,
      width: 275,
      
      borderRadius: 40,

      paddingLeft: 35,
      paddingRight: 35,

      shadowColor: 'black',
      shadowOpacity: 0.40,
      shadowOffset: { width: 10, height: 20},
      shadowRadius: 30,
      elevation: 20,
   },

   alertText:{
        
      color: 'white',
      fontSize: 15,
      fontWeight: 'bold',
   },
   alertInfo:{

      color: 'white',
      fontSize: 15,
      fontWeight: 'bold',
   },

   icon:{

      alignSelf: 'center',
      fontSize : 50,
      color: 'white',

   },

   iconLogout:{

      paddingRight: 10,
      alignSelf: 'flex-end',
      fontSize : 30,
      color: 'white',

   },

   plainText:{
      color: 'white',
      fontSize: 13,
      alignSelf: 'center',
   }
})