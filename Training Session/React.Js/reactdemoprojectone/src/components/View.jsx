
import React, { Component } from 'react'

import Edit from './Edit';
import { Table } from 'semantic-ui-react';

export default class View extends Component {
    render() {
        return (
            <div>

            <Edit></Edit>
            <Table sortable called fixed>
                <Table.Header>
                    <Table.HeaderCell
                </Table.Header>
            </Table>

            </div>
        )
    }
}
