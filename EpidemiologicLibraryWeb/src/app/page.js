'use client'
import {useContext} from "react";
import {LanguageContext} from "@/app/language-context";
import MenuLanguages from "@/app/language";
import Navbar from "@/app/navbar";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faGlobe} from "@fortawesome/free-solid-svg-icons";

export default function Page() {
    const {languageData} = useContext(LanguageContext);

    return (
        <html lang={languageData.definition}>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
                <title>{languageData.title}</title>
            </head>
            <body>
                <div className="sm:flex justify-between items-center bg-my-blue mb-6 pb-1 sm:pb-0 text-white">
                    <h1 className="p-6 text-4xl font-bold">{languageData.title}</h1>
                    <h3 className="flex items-center m-6">
                        <div className="mr-2">
                        <FontAwesomeIcon icon={faGlobe}/>
                        </div>
                        <MenuLanguages/>
                    </h3>
                </div>
                <Navbar/>
            </body>
        </html>
    );
}