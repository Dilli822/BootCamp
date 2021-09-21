
import React, { Component } from 'react';
import { Modal, Form, Button} from 'semantic-ui-react';

export default class Edit extends Component {
    render() {
        return (
            // passing props as true open
            <Modal open={true}>
                <Modal.Header> Edit Your Name Here </Modal.Header>
            <Modal.Content>

                <Form.Field>
                <label>UserName</label>
                <input name="username"/>

                <label>User </label>
                <input name="user"/> 
                <Button type="submit" content="Submit"></Button>
                </Form.Field>
            </Modal.Content>

            </Modal>
        )
    }
}
