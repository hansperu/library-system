import { useNavigate } from "@solidjs/router";
import { createSignal, createMemo, Show, type Component } from "solid-js";
import { ErrorAlert } from "../components/ErrorAlert";
import { signup } from "../utils/users/signup";


export const Signup: Component = () => {
    const [ showPassword, setPassword ] = createSignal<string>("");
    const [ showEmail, setEmail ] = createSignal<string>("");
    const [ showFirstName, setFirstName ] = createSignal<string>("");
    const [ showLastName, setLastName ] = createSignal<string>("");
    const [ showAge, setAge ] = createSignal<string>("");
    const [ showAddress, setAddress ] = createSignal<string>("");
    const [showConfirm, setConfirm] = createSignal<boolean>(false);
    const [ showError, setError ] = createSignal<string>("");
    const navigateLogin = useNavigate()

    createMemo(() => {
        if (showConfirm()) {
            try {
                const user: Object = signup(showEmail(), showPassword(), showFirstName(), showLastName(), parseInt(showAge()), showAddress())
                if (user) {
                    setConfirm(false)
                    navigateLogin("/login")
                }
                setError("")
            } catch (error: any) {
                setError(error.message) 
            }
        }
    })

    return (
        <main class="hero min-h-screen bg-base-200" >
            <div class="hero-content flex-col lg:flex-row-reverse">
                <div class="text-center lg:text-left">
                    <h1 class="text-5xl font-bold">Sign up!</h1>
                    <p class="py-6">Get access to your account to borrow books or return them</p>
                    <Show when={showError()} fallback={<></>}><ErrorAlert message={showError()} /></Show>
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
                        </div>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">First Name</span>
                            </label>
                            <input type="firstName" placeholder="First name" class="input input-bordered" onInput={(e) => setFirstName(e.currentTarget.value)} required />
                        </div>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">Last Name</span>
                            </label>
                            <input type="lastName" placeholder="last name" class="input input-bordered" onInput={(e) => setLastName(e.currentTarget.value)} required />
                        </div>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">age</span>
                            </label>
                            <input type="age" placeholder="age" class="input input-bordered" onInput={(e) => setAge(e.currentTarget.value)} required />
                        </div>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">address</span>
                            </label>
                            <input type="address" placeholder="address" class="input input-bordered" onInput={(e) => setAddress(e.currentTarget.value)} required />
                        </div>
                        <div class="form-control mt-6">
                            <button class="btn btn-primary" onClick={() => setConfirm(true)}>Sign up</button>
                        </div>
                    </form>
                </div>
            </div>
        </main>
    )
}