
import React, { Component } from 'react';
import { Modal, Form, Button} from 'semantic-ui-react';

export default class Edit extends Component {
    
    state = {
        name:"",
        username: "",

    }

    onChangeHandler = (e) => {
        this.setState({ [ e.target.name ] : e.target.value })
    }
    render() {
        const {  name,username } = this.state;
        return (
            // passing props as true open
            <Modal open={false}>
                <Modal.Header> Edit Your Name Here </Modal.Header>
            <Modal.Content>

                <Form.Field>
                <label> Full Name: </label>
                <input
                 value = { username } 
                 name = "username"
                onChange={this.onChangeHandler} />

                <label>Name: </label>
                <input 
                value={name}
                name = "name"
                onChange = {this.onChangeHandler } /> 
                <Button type="submit" content="Submit"></Button>
                </Form.Field>
            </Modal.Content>

            </Modal>
        )
    }
}
