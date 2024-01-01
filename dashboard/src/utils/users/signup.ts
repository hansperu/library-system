

const API_URL = import.meta.env.VITE_API_URL


export const signup = async (email: string, password: string, firstName: string, lastName: string, age: number, address: string) => {
    const response = await fetch(`${API_URL}/users/signup`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password, firstName, lastName, age, address })
    })
    if (!response.ok) {
        throw new Error(response.statusText)
    }

    const data = await response.json()

    return data
}