
import React, { Component } from 'react'

import Edit from './Edit';
import { Table, Button } from 'semantic-ui-react';

export default class View extends Component {

   // let's make function
   onUserDelete = (id) => {
    //passing id for delete
    this.props.onUserDelete(id);
   };

    render() {
        const { data } = this.props;
        // console.log( data );
        return (
            <div>

            <Edit></Edit>
            <Table sortable called fixed>

                <Table.Header>
                    <Table.Row>
                    <Table.HeaderCell>FullName</Table.HeaderCell>
                    <Table.HeaderCell>UserName</Table.HeaderCell>
                    <Table.HeaderCell>Action</Table.HeaderCell>

                    </Table.Row>
                    </Table.Header>

                    <Table.Body>

                        {
                            data.map((user)=> (
                                
                            <Table.Row>
                            <Table.Cell>{ user.name }</Table.Cell>
                            <Table.Cell>{ user.username} </Table.Cell>
                            <Table.Cell>
                                <Button content="Edit"></Button>
                                <Button content="Delete" onClick = 
                                {this.onUserDelete.bind(this, user.id) }></Button>
                            </Table.Cell>
                        </Table.Row>

                        ))}
                      
                        

                    </Table.Body>
            </Table>

            </div>
        )
    }
}
