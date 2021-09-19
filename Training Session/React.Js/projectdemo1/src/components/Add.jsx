
import React, { Component } from 'react'
import { Button, Form, Header, Modal , Checkbox} from 'semantic-ui-react'

export default class Add extends Component {
    state = {
        name: "",
        usename: "",
    };

    render() {
        const {user, username} = this.state;
        return (
            <Modal
            trigger={<Button>Add a New User</Button>}
          >
            <Header icon='archive' content='Archive Old Messages' />
            <Modal.Content>
              <p>
                Your inbox is getting full, would you like us to enable automatic
                archiving of old messages?
              </p>

              <Form>

                  <Form.Field>
                      <label>First Name</label>
                      <input placeholder='Full Name ' value={user} />
                      </Form.Field>

                      <Form.Field>
                           <label>Last Name</label>
                           <input placeholder='UserName' value={username} />
                            </Form.Field>

                             <Form.Field>
                                  <Checkbox label='Remeber Me' />
                                  </Form.Field>
                                   <Button type='submit'>Submit</Button>
                                   </Form>
            </Modal.Content>
            </Modal>
           
                )
    }
}
