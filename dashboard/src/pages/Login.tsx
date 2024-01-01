import type { Component } from "solid-js";
import { createMemo, createSignal, Show } from "solid-js";
import { login } from "../utils/users/login";

import { ErrorAlert } from "../components/ErrorAlert";
import { useNavigate } from "@solidjs/router";
import { NavBar } from "../components/NavBar";


export const Login: Component = () => {
    const [showEmail, setEmail] = createSignal<string>("");
    const [showPassword, setPassword] = createSignal<string>("");
    const [showConfirm, setConfirm] = createSignal<boolean>(false);
    const [showError, setError] = createSignal<string>("");
    const navigateDashboard = useNavigate()

    createMemo(() => {
        if (showConfirm()) {
                login(showEmail(), showPassword()).then((token: string) => {
                    localStorage.setItem("token", token)
                    setConfirm(false)
                    setError("")
                    navigateDashboard("/dashboard")
                }).catch((error: any) => setError(error.message))
        }
    })
    return (
        <>
            <NavBar/>
            <main class="hero min-h-screen bg-base-200" >
                <div class="hero-content flex-col lg:flex-row-reverse">
                    <div class="text-center lg:text-left">
                        <h1 class="text-5xl font-bold">Login now!</h1>
                        <p class="py-6">Get access to your account to borrow books or return them</p>
                        <div>
                            <h1>Not yet registered?</h1>
                            <a class="link" href="/signup">Sign up</a>
                        </div>
                    <Show when={showError()} fallback={<></>}>
                        <div class="flex justify-center items-center w-full h-full p-4">
                            <ErrorAlert message={showError()} />
                        </div>
                    </Show>
                    </div>
                    <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                        <form class="card-body">
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Email</span>
                                </label>
                                <input type="email" placeholder="email" class="input input-bordered" onInput={(e) => setEmail(e.currentTarget.value)} required />
                            </div>
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Password</span>
                                </label>
                                <input type="password" placeholder="password" class="input input-bordered" onInput={(e) => setPassword(e.currentTarget.value)} required />
                                <label class="label">
                                    <a href="/" class="label-text-alt link link-hover">Forgot password?</a>
                                </label>
                            </div>
                            <div class="form-control mt-6">
                                <button type="button" class="btn btn-primary" onClick={() => setConfirm(true)}>Login</button>
                            </div>
                        </form>
                    </div>
                </div>
            </main>
        </>
    )
}