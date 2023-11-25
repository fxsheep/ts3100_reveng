# Memory Maps


## System memory map
|   Start    |    End     |    Wrap    |    Name    |    Notes     |
|------------|------------|------------|------------|--------------|
| 0x00000000 | 0x03FFFFFF | 0x3FFFFFFF |    DRAM    |              |
| 0xC0000000 | 0xCFFFFFFF |    -/?     |    MMIO    |              |
| 0xE0000000 |     ?      |    -/?     |     ?      |              |
| 0xF0000000 | 0xF03FFFFF | 0xF7FFFFFF |    XIP0    |   GD25Q32C   |
| 0xF8000000 | 0xF87FFFFF | 0xFFFFFFFF |    XIP1    |   GD25Q64C   |

## GD25Q32C flash layout
|  Start   |   End    |   Name   |
|----------|----------|----------|

## GD25Q64C flash layout
|  Start   |   End    |   Name   |
|----------|----------|----------|
| 0x000000 | 0x03FFFF |  Config  |
| 0x040000 | 0x7EFFFF | Firmware |
| 0x7F0000 | 0x7FFFFF |   Boot   |

## Notes
 - arm boot vector: 0xFFFF0000 -> GD25Q64C 0x7F0000
