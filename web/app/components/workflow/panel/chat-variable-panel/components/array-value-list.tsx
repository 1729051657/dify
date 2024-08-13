'use client'
import type { FC } from 'react'
import React, { useCallback } from 'react'
import { useTranslation } from 'react-i18next'
import { RiAddLine } from '@remixicon/react'
import produce from 'immer'
import RemoveButton from '@/app/components/workflow/nodes/_base/components/remove-button'
import Button from '@/app/components/base/button'

type Props = {
  isString: boolean
  list: any[]
  onChange: (list: any[]) => void
}

const ArrayValueList: FC<Props> = ({
  isString = true,
  list,
  onChange,
}) => {
  const { t } = useTranslation()

  const handleNameChange = useCallback((index: number) => {
    return (e: React.ChangeEvent<HTMLInputElement>) => {
      const newList = produce(list, (draft: any[]) => {
        draft[index] = isString ? e.target.value : Number(e.target.value)
      })
      onChange(newList)
    }
  }, [isString, list, onChange])

  const handleItemRemove = useCallback((index: number) => {
    return () => {
      const newList = produce(list, (draft) => {
        draft.splice(index, 1)
      })
      onChange(newList)
    }
  }, [list, onChange])

  const handleItemAdd = useCallback(() => {
    const newList = produce(list, (draft: any[]) => {
      draft.push(undefined)
    })
    onChange(newList)
  }, [list, onChange])

  return (
    <div className='w-full space-y-2'>
      {list.map((item, index) => (
        <div className='flex items-center space-x-1' key={index}>
          <input
            className='block px-3 w-full h-8 bg-components-input-bg-normal system-sm-regular radius-md border border-transparent appearance-none outline-none caret-primary-600 hover:border-components-input-border-hover hover:bg-components-input-bg-hover focus:bg-components-input-bg-active focus:border-components-input-border-active focus:shadow-xs placeholder:system-sm-regular placeholder:text-components-input-text-placeholder'
            placeholder={t('workflow.chatVariable.modal.arrayValue') || ''}
            value={list[index]}
            onChange={handleNameChange(index)}
            type={isString ? 'text' : 'number'}
          />
          <RemoveButton
            className='!p-2 !bg-gray-100 hover:!bg-gray-200'
            onClick={handleItemRemove(index)}
          />
        </div>
      ))}
      <Button variant='tertiary' className='w-full' onClick={handleItemAdd}>
        <RiAddLine className='mr-1 w-4 h-4' />
        <span>{t('workflow.chatVariable.modal.addArrayValue')}</span>
      </Button>
    </div>
  )
}
export default React.memo(ArrayValueList)