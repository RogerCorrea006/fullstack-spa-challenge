import axios from 'axios';

const apiUrl = 'http://127.0.0.1:5001'

const axiosInstance = axios.create({
  baseURL: apiUrl,
  timeout: 1000,
  headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', }
});

export default axiosInstance;