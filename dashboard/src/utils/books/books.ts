import { API_URL } from '../../config'
import { BookSchema } from '../../components/BookCard'
import { Output} from 'valibot'


export async function getBooks(): Promise<Output<typeof BookSchema>[]> {
    try {

        const response = await fetch(`${API_URL}/books`,)
        if (!response.ok) {
            throw new Error(response.statusText)
        }

        const data = await response.json()

        return data
    } catch (error) {
        console.error(error)
        return []
    }
}

