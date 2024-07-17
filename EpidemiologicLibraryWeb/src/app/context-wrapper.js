'use client'
import LanguageProvider from "./language-context";

export default function ContextWrapper({children}) {
    return (
        <LanguageProvider>
            {children}
        </LanguageProvider>
    );
}