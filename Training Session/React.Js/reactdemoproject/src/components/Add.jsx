
import React, { Component } from 'react'
import { Button, Form, Modal , Checkbox} from 'semantic-ui-react'
import { v4 as uuidv4 } from 'uuid';

export default class Add extends Component {
    state = {
        // add name value for testing
         id: uuidv4(),
        name: "",
        usename: "",
    };

    // event handler
    onInputChange = (event) => {
        this.setState({
        // setting the state her
       [event.target.name]: event.target.value,
        });
        // console.log(event.target.value);
        console.log(event.target.name);
        // console.log(event.target.username);

    };

    // submit method
    onFormSubmit = (event) => {
        // preventDefault method will stop the browser refreshing the page
        // after the submission of form
        event.preventDefault();
        this.props.onSubmit(this.state);
        this.setState({name:"", username: ""})
        console.log('form is successfully submitted!')
    };

    render() {
        const {name,username} = this.state;
        return (
            <Modal
            trigger={<Button>Add a New User</Button>}
          >
            <Modal.Content>
              <h3>
                Want to add a new user please fill the box below!
              </h3>

              <Form onSubmit={this.onFormSubmit}>

                  <Form.Field>
                      <label>Full Name</label>
                      <input name="name" onChange={this.onInputChange} placeholder='Full Name' value={name}/>
                      </Form.Field>

                      <Form.Field>
                           <label>UserName</label>
                           <input name="username"  onChange={this.onInputChange} placeholder='UserName' value={username} />
                            </Form.Field>

                             <Form.Field>
                                  <Checkbox label='Remember Me' />
                                  </Form.Field>
                                   <Button type='submit'>Submit</Button>
                                   </Form>
            </Modal.Content>
            </Modal>
           
                )
    }
}
