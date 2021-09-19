
import React, { Component } from 'react'
import Add from  './components/Add';
import View from './components/View';
import { Container} from 'semantic-ui-react';
import { Input } from 'semantic-ui-react';

export default class App extends Component {
 //keeping objects in the state
  state = {
    users: [
      {id: 1, name: "Dilli Hang Rai", username: "Dilli"},
      {id: 2, name: "Rachel Singh", username: "Rachel"},
      {id: 3, name: "Hari Bahadur", username: "Hari"},
    ],
  };
  // function must be at the top
  onSearchChange = (event) =>{
    console.log(event.target.value)
  }
  render() {

    // 
    const { users } =this.state;
    console.log(users)
    return (

      <Container>
        <Add></Add>
        <Input icon="search" placeholder="search" onChange={this.onSearchChange}></Input>
        <View data={ users }>

        </View>
      </Container>
        
    )
  }
}
