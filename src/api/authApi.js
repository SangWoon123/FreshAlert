import axios from 'axios'

const VITE_APP_SERVER_URI = import.meta.env.VITE_APP_SERVER_URI

export const authInstance = (url) => {
  const instance = axios.create({
    baseURL: VITE_APP_SERVER_URI + url,
    timeout: 10000
  })

  return instance
}
