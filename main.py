from pymem import Pymem
import pymem.process, os, time

sent = False

def resolve_pointer_chain(pm, base, offsets):
    addr = pm.read_longlong(base)
    for offset in offsets[:-1]:
        addr = pm.read_longlong(addr + offset)
    return addr + offsets[-1]

while True:
    try:
        pm = Pymem("javaw.exe")

        openal_module = pymem.process.module_from_name(pm.process_handle, "OpenAL64.dll")
        openal_base = openal_module.lpBaseOfDll

        x_base = openal_base + 0x5C308
        y_base = openal_base + 0x5C308
        z_base = openal_base + 0x5C308

        x_offsets = [0x8, 0x8]
        y_offsets = [0x8, 0x4]
        z_offsets = [0x8, 0x0]

        x_addr = resolve_pointer_chain(pm, x_base, x_offsets)
        y_addr = resolve_pointer_chain(pm, y_base, y_offsets)
        z_addr = resolve_pointer_chain(pm, z_base, z_offsets)

        sent = False

        while True:
            try:
                x_val = pm.read_float(x_addr)
                y_val = pm.read_float(y_addr)
                z_val = pm.read_float(z_addr)
                os.system('cls' if os.name == 'nt' else 'clear')
                box = [
                    "======================================================================",
                    "=                                                                    =",
                    "=  __   __           _ _     __        _                             =",
                    "=  \ \ / /          (_|_)   / /       | |                            =",
                    "=   \ V / __ _ _ __  _ _   / /__  __ _| | ___   _ _ __ ___   ___     =",
                    "=    > < / _` | '_ \| | | / / __|/ _` | |/ / | | | '__/ _ \ / _ \    =",
                    "=   / . \ (_| | | | | | |/ /\__ \ (_| |   <| |_| | | | (_) | (_) |   =",
                    "=  /_/ \ \_\__,_|_|_|_|_|_/ |___/\__|_|_|_\\\\____,|_|  \___/ \___/    =",
                    "=                                                                    =",
                    "=                               v1.0.0                               =",
                    "======================================================================"
                ]

                for line in box:
                    print(f"\033[94m{line}\033[0m")
                print(f"\n\n\nCurrent Position:                                    Socials:\n  X: {x_val:.5f}                            https://www.youtube.com/Xanii\n  Y: {y_val:.5f}                             https://Twitter.com/_Xanii_\n  Z: {z_val:.5f}                            https://github.com/LXanii/")
                time.sleep(0.1)
            except Exception as e:
                print("Memory read failed:", e)
                break
    except Exception as e:
        if sent == False:
            sent = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Open Minecraft (Inf Dev)")
            print(f"{e}")