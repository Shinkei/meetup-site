import axios from 'axios'

const client = axios.create({
  method: 'post',
  url: `${process.env.API_BASE_URL}/graphql`
})

client.interceptors.request.use((config) => {
  const token = window.localStorage.getItem('auth_token')
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

export default (query) => client.request({data: {query}})
