
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
  // new set query
  // for search fuction
  query: "",
  results: [],
  };

  


  // on user delet function
  onUserDelete = (id) => {
    const{ users } = this.state;
    this.setState({
      users: users.filter((user) => 
      user.id !== id ),
    });
  };
    // function must be at the top
  // onSearchChange = (event) =>{
  //   console.log(event.target.value)
  // }


  // onSearch Function live
  // capturing event value in vriable value
  onSearchChange = (event) => {
    // console.log(event.target.value);
    const value = event.target.value;
    const { users } = this.state;
    this.setState({ query: value });

    // regex will match the value of query and event
    const results = users.filter(( user)=>{
      const regex = new RegExp(value, "gi");
      return user.name.match(regex)
    });
    // do results: {results }
    console.log(results);
    this.setState({ results }); 
  };
  // // argu user from View.jsx
  onFormSubmit = (user) => {
    console.log(user)
    const {users} = this.state;
    this.setState({users: [...users, user]});
  };


  getUserById=(id)=>{
    const {users}=this.state
    const user = users.filter((user)=>user.id === id);
    return user[0];
  }
  onEdit=(id,updatedUser)=>{
    const { users } = this.state;
    this.setState({
    users:users.map((user)=> user.id === id ? updatedUser : user)
    });
  };

  render() {
    const { users, results, query } =this.state;
    const data = results.length===0 && !query ? users : results;
    // console.log(users)
    return (

      <Container>
        <Add onSubmit={this.onFormSubmit}></Add>
        <Input icon="search" placeholder="search" onChange={this.onSearchChange}></Input>
        <View data = { data } onUserDelete = { this.onUserDelete } getUserById = {this.getUserById} onEdit={this.onEdit}>
        </View>
      </Container>
        
    )
  }
}
