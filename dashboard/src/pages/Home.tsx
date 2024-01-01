import type { Component } from 'solid-js'
import { NavBar } from '../components/NavBar'




export const Home: Component = () => {
    return (
        <>
            <NavBar/>
            <main class="hero min-h-screen" style="background-image: url(https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi2-prod.mirror.co.uk%2Fincoming%2Farticle13150515.ece%2FALTERNATES%2Fs1227b%2F0_PAY-Clock-over-door-to-Honby-library-Liverpool-central-library-Picton-reading-rooms.jpg);">
                <div class="hero-overlay bg-opacity-60"></div>
                <div class="hero-content text-center text-neutral-content">
                    <div class="max-w-md">
                        <h1 class="mb-5 text-5xl font-bold">Welcome to the library system</h1>
                        <p class="mb-5">Dive into an extensive library at your fingertips. Welcome to the vast collection of books from various authors. Whether you're a classic literature enthusiast or a fan of contemporary fiction, our platform caters to all your reading preferences.</p>
                        <a class="btn btn-primary" href="/login">Get Started</a>
                    </div>
                </div>
            </main>
        </>
    )
}