
import React from "react";

// function App() {
//   return (
//     <div className="App">
//       Hello this is react app
//     </div>
//   );
// };

// class Based Component
// lets create a counter app  
class App extends React.Component{
  // class based comp must have start which holds temporary data
  state = {
    count: 0,
  }

  // function for increment and decrement and reset
  handleInc = () => {
    // setState method will call the state and rerender the component
    this.setState({count: this.state.count + 1});
  };

  handleDec = () => {
    this.setState({count: this.state.count - 1});
  };

  handleRes = () =>{
    this.setState({count: 0});
  };


  render(){
    return (
      <div>
        {/* accessing the class state with this helper  */}
        <h2>The Counter value is:{this.state.count}</h2>
        <button onClick={this.handleInc}> Increment</button>
        <button onClick={this.handleRes}> Reset </button>
        <button onClick={this.handleDec}> Decrement </button>
      </div>

    );
  };
};

export default App;
