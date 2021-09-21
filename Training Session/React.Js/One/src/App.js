
import React, { Component } from 'react'
import Add from  './components/Add';
import View from './components/View';
import { Container} from 'semantic-ui-react';
import { Input } from 'semantic-ui-react';

export default class App extends Component {
 //keeping objects in the state
  state = {
    users: [
      {id: 1, name: "dilli", username: "dilli8222"},
      {id: 2, name: "sita rai", username: "sita"},
      {id: 3, name: "hari bahadur", username: "hari"},
    ],
  };
  // function must be at the top
  onSearchChange = (event) =>{
    console.log(event.target.value)
  }
  render() {
    return (

      <Container>
        <Add></Add>
        <Input icon="search" placeholder="search" onChange={this.onSearchChange}></Input>
        <View></View>
      </Container>
        
    )
  }
}
