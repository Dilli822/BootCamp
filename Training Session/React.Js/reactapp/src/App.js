
// import React from "react";

// function App() {
//   return (
//     <div className="App">
//       Hello this is react app
//     </div>
//   );
// };

// class Based Component
// lets create a counter app  
// class App extends React.Component{
//   // class based comp must have start which holds temporary data
//   state = {
//     count: 0,
//   }

//   // function for increment and decrement and reset
//   handleInc = () => {
//     // setState method will call the state and rerender the component
//     this.setState({count: this.state.count + 1});
//   };

//   handleDec = () => {
//     this.setState({count: this.state.count - 1});
//   };

//   handleRes = () =>{
//     this.setState({count: 0});
//   };

  
//   render(){
//     return (
//       <div>
//         {/* accessing the class state with this helper  */}
//         <h2>The Counter value is:{this.state.count}</h2>
//         <button onClick={this.handleInc}> Increment</button>
//         <button onClick={this.handleRes}> Reset </button>
//         <button onClick={this.handleDec}> Decrement </button>
//       </div>

//     );
//   };
// };

// Above we made a simple app button of increment, decrement and reset

// export default App;

// What is RCC react?
// rcc→ class component skeleton. rrc→ class component
// skeleton with react-redux connect.

// list and props
//  we used appone  in inex.js so we use appone here as comp
import React, { Component } from 'react'
import { render } from 'react-dom'

import Profile from './components/Profile'

export default class AppOne extends Component {

    // state for props
    // inserting the array of userdetails inside it
    // this is hardcore state array data
 state = [
  {
     id: 1,
     name: "dilli",
     img: "https://avatars.githubusercontent.com/u/76522863?v=4",
     description: "Recently Visited Your Profile! ",
  },


  {
      id: 2,
      name: "Hari",
      img: "https://unsplash.it/61",
      description: "Wants to Poke You!",
  },

  {
      id: 3,
      name: "Rachel",
      img: "https://unsplash.it/62",
      description: "Last Seen watching avatar anime",
  },


  {
      id: 4,
      name: "Ram Bahadur",
      img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDVUC8nXJirk63o2pDvW935GLbAb2hOi1DIg&usqp=CAU",
      description: "VC living Legend Gurkha Warrior ",
  },
  {
    id: 5,
    name: "avatar",
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMa6Pi7u9IPD6JJVo5-OEhFQw_4EYcd-4uWg&usqp=CAU",
    description: "Avatar cartoon image"
  }
  ];

  // render() {
  //   return (
  //     <div>
  //       <h2>This is main div component!</h2>
  //       <Profile /> 
  //     </div>
  //   )
  // }

render() {
  return (
    <div>
      {this.state.map((profile) => {
        // let's pass props 
        return <Profile profileprops={profile} key={profile.id} />
        // after deletion it should know it donot render
        // now profile id will be unique each time
      })}
    </div>
  );
 }
 }

