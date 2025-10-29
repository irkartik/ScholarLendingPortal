import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Equipment API calls
export const equipmentAPI = {
  getAll: () => api.get('/equipment/'),
  getById: (id) => api.get(`/equipment/${id}/`),
  create: (data) => api.post('/equipment/', data),
  update: (id, data) => api.put(`/equipment/${id}/`, data),
  delete: (id) => api.delete(`/equipment/${id}/`),
  getAvailable: (id) => api.get(`/equipment/${id}/available/`),
};

// Lending Records API calls
export const lendingAPI = {
  getAll: (params) => api.get('/lending-records/', { params }),
  getById: (id) => api.get(`/lending-records/${id}/`),
  create: (data) => api.post('/lending-records/', data),
  update: (id, data) => api.put(`/lending-records/${id}/`, data),
  delete: (id) => api.delete(`/lending-records/${id}/`),
  approve: (id) => api.post(`/lending-records/${id}/approve/`),
  returnEquipment: (id) => api.post(`/lending-records/${id}/return_equipment/`),
};

export default api;
