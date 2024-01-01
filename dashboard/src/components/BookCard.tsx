import type { Component } from "solid-js";
import { object, string, number, type Output } from "valibot";

export const BookSchema = object({
    id: number(),
    title: string(),
    author: string(),
    portrait: string()
})

type BooksProps = {
    Book: Output<typeof BookSchema>,
}


export const BookCard: Component<BooksProps> = (props) => {
    const { Book } = props;
    return (
        <div class="card w-96 bg-base-100 shadow-xl image-full my-4">
            <figure><img src={Book.portrait} alt="Cover" /></figure>
            <div class="card-body">
                <h2 class="card-title">{Book.title}</h2>
                <p>{Book.author}</p>
                <div class="card-actions justify-end">
                    <button class="btn btn-primary">Borrow</button>
                </div>
            </div>
        </div>
    )
}