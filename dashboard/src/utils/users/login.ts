

const API_URL = import.meta.env.VITE_API_URL


export async function login(email: string, password: string) {
    const response = await fetch(`${API_URL}/users/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
    if (!response.ok) {
        throw new Error(response.statusText)
    }

    const data = await response.json()

    return data.token
}