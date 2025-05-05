import axios from 'axios'

const VITE_ENV_URI = {
  login: import.meta.env.VITE_APP_LOGIN_URI,
  products: import.meta.env.VITE_APP_PRODUCTS_URI,
  productNames: import.meta.env.VITE_APP_PRODUCT_NAMES_URI,
  categories: import.meta.env.VITE_APP_CATEGORIES_URI,
  addProduct: import.meta.env.VITE_APP_ADD_PRODUCT_URI,
  addProductName: import.meta.env.VITE_APP_ADD_PRODUCT_NAME_URI,
  deleteProductName: import.meta.env.VITE_APP_DELETE_PRODUCT_NAME_URI
}

export const authInstance = (url, timeout = 10000) => {
  const instance = axios.create({
    baseURL: url,
    timeout: timeout
  })

  return instance
}

export const loginAPI = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.login,
    timeout: 10000
  })

  return instance
}

export const getProducts = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.products,
    timeout: 60000
  })

  return instance
}

export const getProductNames = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.productNames,
    timeout: 10000
  })

  return instance
}

export const getCategories = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.categories,
    timeout: 10000
  })

  return instance
}

export const addProduct = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.addProduct,
    timeout: 10000
  })

  return instance
}

export const addProductName = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.addProductName,
    timeout: 10000
  })

  return instance
}

export const deleteProductName = () => {
  const instance = axios.create({
    baseURL: VITE_ENV_URI.deleteProductName,
    timeout: 10000
  })

  return instance
}
