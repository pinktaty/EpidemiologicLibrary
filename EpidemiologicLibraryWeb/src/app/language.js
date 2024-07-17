import {useContext, useState} from "react";
import {LanguageContext} from "./language-context";
import Image from "next/image";

export default function MenuLanguages() {
    const [open, setOpen] = useState(false);
    const {changeLanguage} = useContext(LanguageContext);

    const toggleMenu = () => {
        setOpen(!open);
    };

    const changeLanguageAux = (language) => {
        changeLanguage(language);
        toggleMenu();
    }

    const {languageData} = useContext(LanguageContext);

    // TODO: Sobreponer el menú a los elementos. (Por mejorar)

    const createButtons = (languages) => {
        const buttons = [];

        for(let i = 0; i < languages.length; i++) {
            buttons.push(
                <button onClick={() => changeLanguageAux(`${languages[i]}`)}
                        className="sm:my-1 w-full text-center rounded-md p-2 text-sm hover:bg-gray-500 hover:text-white">
                    <Image className="absolute" src={`./languages/${languages[i]}.svg`} alt={`${languageData.language.types[i]}`}  width={20} height={20}/>
                    <span className="ml-5">{languages[i]}</span>
                </button>
            );
        }
        return buttons;
    }

    return (
        <div className="relative inline-block text-left">
            <button onClick={toggleMenu}
                    className="flex items-center mr-1.5 text-lg">{languageData.language.title}</button>
            <div className={`${open ? 'block' : 'hidden'} absolute mt-2 right-0 w-22 sm:mt-3 bg-my-blue rounded p-1`}>
                {createButtons(["es", "en"])}
            </div>
        </div>
    );
}