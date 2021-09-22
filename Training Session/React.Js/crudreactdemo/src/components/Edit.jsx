
import React, { Component } from 'react';
import { Modal, Form, Button} from 'semantic-ui-react';

export default class Edit extends Component {
    
    state = {
        name:"",
        username: "",

    }

    componentDidUpdate(prevProps) {
    if (prevProps.id !== this.props.id){
        const user = this.props.getUserById(this.props.id)
        this.setState({
                name:user.name,
                username:user.username,
            })
        }
    };

    onChangeHandler = (e) => {
        this.setState({ [ e.target.name ] : e.target.value })
    }

    onCloseClick = () => {
        this.props.onClose()
    }
    render() {
        const {  name,username } = this.state;
        const { isOpen } = this.props;
        return (
            // passing props as true open
            <Modal open={ isOpen } onClose={this.onCloseClick}>
                <Modal.Header> Edit Your Name Here </Modal.Header>
            <Modal.Content>

                <Form.Field>
                <label> Full User Name: </label>
                <input
                 value = { username } 
                 name = "username"
                onChange={this.onChangeHandler} />

                <label>  Name: </label>
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
