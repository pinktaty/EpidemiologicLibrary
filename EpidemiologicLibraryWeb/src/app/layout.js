import "./globals.css";
import ContextWrapper from "@/app/context-wrapper";
import Page from "@/app/page";

export default function RootLayout() {
  return (
      <ContextWrapper>
        <Page/>
      </ContextWrapper>
  );
}
