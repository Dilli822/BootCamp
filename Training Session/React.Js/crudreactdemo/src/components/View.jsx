
import React, { Component } from 'react'

import Edit from './Edit';
import { Table, Button } from 'semantic-ui-react';

export default class View extends Component {

    state = {
        isOpen: false,
        id: "",
    };

   // let's make function
   onUserDelete = (id) => {
    //passing id for delete
    this.props.onUserDelete(id);
   };


   //onEditClick
   onEditClick = (id) => {
       this.setState ({ isOpen: true , id: id})
   };

   onCloseClick = () => {
       this.setState({
           isOpen: false,
       })
   };

   

    render() {
        // eslint-disable-next-line 
        const { data, getUserById } = this.props;
        const { isOpen, id } = this.state;

        return (
            <div>

            <Edit isOpen = { isOpen } onClose = { this.onCloseClick } id = { id } getUserById = {getUserById}></Edit>
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
                                <Button content="Edit"  onClick={this.onEditClick.bind(this, user.id)}></Button>
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
