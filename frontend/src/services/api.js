import axios from 'axios';

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_BASE_URL ||
    'https://governmentanomalydetection.onrender.com/api/v1',
});

export default api;