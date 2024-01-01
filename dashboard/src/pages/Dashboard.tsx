import type { Component } from "solid-js";
import {For, createResource} from "solid-js";


import { BookCard, BookSchema } from "../components/BookCard";
import { getBooks } from "../utils/books/books";
import { parse } from "valibot";



export const Dashboard: Component = () => {
    const [books] = createResource(getBooks)
    return (
        <main>
            <h1>Dashboard</h1>
            <For each={books()}>{(book) => <BookCard Book={parse(BookSchema, book)} />}</For>
        </main>
    )
}