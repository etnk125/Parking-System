import axios from "axios";

const URL = "http://localhost:5000";
const client = axios.create({
  baseURL: URL,
});

export async function login(body) {
  return await client.post("/login", body);
}
export async function register(body) {
  return await client.post("/register", body);
}
export async function reserve() {
  return await client.post("/reserve/A1/123");
}
export async function checkout() {
  return await client.post("/checkout/A1");
}
