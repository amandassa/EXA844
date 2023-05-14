import React, { useState } from 'react';
import {
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    Input
  } from '@chakra-ui/react'

function MessageRow({ message }) {
    return (
        <Tr>
        <Td>{message[0]}</Td>
        <Td>{message[1]}</Td>
        <Td>{message[2]}</Td>
        </Tr>
    );
}

function SearchBar({ filterText, onFilterTextChange }) {
    return (
        <form>
        <Input
            type="text"
            value={filterText}
            placeholder="Buscar..."
            onChange={(e) => onFilterTextChange(e.target.value)}
        />
        </form>
    );
}
  
function MessageTable({ messages, filterText }) {
    const rows = [];
    messages.map((message) => {
        let messageLC = message.map((column) => typeof column === 'string' ? column.toLowerCase() : column )
        if (messageLC.includes(filterText.toLowerCase()) || filterText === "") {
            rows.push(<MessageRow message={message} />);
        }
    });

    return (
        <Table variant="striped">
            <Thead>
                <Tr>
                    <Th>Author</Th>
                    <Th>Message</Th>
                    <Th>Date</Th>
                </Tr>
            </Thead>            
            <Tbody>{rows}</Tbody>
        </Table>
    );
}
  
function FilterableMessagesTable({ messages }) {
    const [filterText, setFilterText] = useState("");

    return (
        <div>
        <SearchBar filterText={filterText} onFilterTextChange={setFilterText} />
        <MessageTable messages={messages} filterText={filterText} />
        </div>
    );
}

export { FilterableMessagesTable };