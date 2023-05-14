"use client"; 

import React, { useState } from 'react';
import styles from "./page.module.css";
import { ChakraProvider } from '@chakra-ui/react'
import { FilterableMessagesTable } from './components';

//Coloque o código dos demais componentes aqui...
export default function Home() {
    
  const [blogMessages, setBlogMessages] = useState([]);
  
  fetch('https://script.google.com/macros/s/AKfycbzBn3sALe1rYjz7Ze-Ik7q9TEVP0I2V3XX7GNcecWP8NvCzGt4yO_RT1OlQp09TE9cU/exec')
    .then(response => response.json())
    .then(data => {
        setBlogMessages(data);
        console.log(data)
    });
    
    return (
      <ChakraProvider>
        <main className={styles.main}>
          <FilterableMessagesTable messages={blogMessages} />
        </main>

      </ChakraProvider>
    )
}

