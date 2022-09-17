import styles from '../styles/Home.module.css'
import Head from "next/head";
import Image from "next/image";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
    const [data, setData] = useState([{}]);
    useEffect(()=>{
        fetch("http://localhost:8000")
        .then((res)=>res.json)
        .then((data)=>{
            setData(data);
            console.log(data);
        });

//         const reservedBookState  = ()=>axios.get("http://localhost:8000/"
// ).then((res)=>{
// 	console.log(`${res.data}`);
// }).catch(function(error){
// 	console.log(` ${error.response.status}`);
// });
    },[]);
    return<div></div>
}