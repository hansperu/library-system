import type { Component } from "solid-js";


export const NotFound: Component = () => {
    return (
        <main class="hero min-h-screen bg-base-200">
            <div class="hero-content text-center">
                <div class="max-w-md">
                    <h1 class="text-5xl font-bold">404</h1>
                    <p class="py-6">Page not found</p>
                </div>
            </div>
        </main>
    )
}