const API_URL = "http://localhost:8000";

export async function apiFetch(endpoint: string, options?: RequestInit) {
    const response = await fetch(`${API_URL}${endpoint}`,{
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            ...(options?.headers || {})
        },
        ...options
    });
    if(!response.ok){ 
        throw new Error("Api request failed with status: " + response.status);
    }
    return response.json();
}