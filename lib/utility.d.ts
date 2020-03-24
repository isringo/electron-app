interface Utility {
    electron: any
}

// NodeJS.Global 拡張
declare namespace NodeJS {
    interface Global extends Utility {
    }
}

// Window 拡張
interface Window extends Utility {
}

declare var global: NodeJS.Global;
declare var window: Window & typeof globalThis;